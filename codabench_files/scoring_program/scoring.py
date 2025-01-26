import sys
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from functools import reduce

# Directory to read labels from
input_dir = sys.argv[1]
solutions = os.path.join(input_dir, 'ref')
prediction_dir = os.path.join(input_dir, 'res')

# Directory to output computed score into
output_dir = sys.argv[2]


def read_prediction():
    prediction_file = os.path.join(prediction_dir,'test.predictions')

    # Check if file exists
    if not os.path.isfile(prediction_file):
        print('[-] Test prediction file not found!')
        print(prediction_file)
        return
    
    # Read the prediction file
    return  pd.read_pickle(prediction_file)


def get_t_and_anomaly_data(solution_file, location):
    # Check if file exists
    if not os.path.isfile(solution_file):
        print('[-] Test solution file not found!')
        return

    # Read the solution file
    df = pd.read_csv(solution_file)
    df = df[['t', 'anomaly']].rename(columns={'anomaly': location})
    df['t'] = pd.to_datetime(df['t'], format='%Y-%m-%d')
    return df

def read_solution():

    print(os.listdir(solutions))

    # Load all locations files 
    # Order of the files matter
    list_of_locations = ['Atlantic_City', 'Baltimore', 'Eastport', 'Fort_Pulaski', 'Lewes', 
                         'New_London', 'Newport', 'Portland', 'Sandy_Hook', 'Sewells_Point', 'The_Battery', 'Washington' 
    ]


    test_answer_location = [get_t_and_anomaly_data(os.path.join(solutions, location + '_2008_2013_answer_data.csv'), location) for location in list_of_locations] 

    df_merged = df_merged = reduce(lambda left, right: pd.merge(left, right, on='t', how='inner'), test_answer_location)

    return df_merged


def save_score(f1_t_only, f1_t_and_location, final_grade):
    score_file = os.path.join(output_dir, 'scores.json')

    scores = {
        'F1-Score': f1_t_only,
        'F1-Score with location': f1_t_and_location,
        'Final Grade': final_grade
    }
    with open(score_file, 'w') as f_score:
        f_score.write(json.dumps(scores))
        f_score.close()


def print_pretty(text):
    print("-------------------")
    print("#---",text)
    print("-------------------")


    
def main():

    # Read prediction and solution
    print_pretty('Reading prediction')
    prediction = read_prediction()
    solution = read_solution()

    if solution.isnull().values.any():
        print('[-] Solution contains NaN values')
        return

    # Check if there is any anomaly in the prediction
    solution['anomaly'] = (solution.drop(columns='t') == 1).any(axis=1)
    prediction['anomaly'] = (prediction.drop(columns='time') == 1).any(axis=1)

    print(solution)
    # solution.rename(columns={'t': 'time'}).to_pickle('solution.pkl')
    print(prediction)

    # Compute Score
    print_pretty('Computing score')
    f1_t_only = f1_score(solution['anomaly'], prediction['anomaly'])


    list_of_locations = ['Atlantic_City', 'Baltimore', 'Eastport', 'Fort_Pulaski', 'Lewes', 
                         'New_London', 'Newport', 'Portland', 'Sandy_Hook', 'Sewells_Point', 'The_Battery', 'Washington' 
    ]

    # F1-score based on both 't' and 'location' columns
    f1_t_and_location = [f1_score(solution[location], prediction[location]) for location in list_of_locations]

    f1_t_and_location = np.mean(f1_t_and_location)

    # Calculate the final grade with weightages
    final_grade = (0.3 * f1_t_only) + (0.7 * f1_t_and_location)

    # Print the results
    print(f"F1-Score based only on 't': {f1_t_only:.4f}")
    print(f"F1-Score based on 't' and 'location': {f1_t_and_location:.4f}")
    print(f"Final Grade: {final_grade:.4f}")

    # Write Score
    print_pretty('Saving prediction')
    save_score(f1_t_only, f1_t_and_location, final_grade)

if __name__ == '__main__':
    main()
