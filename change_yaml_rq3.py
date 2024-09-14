import yaml
import sys

if __name__ == "__main__":

    algorithm = sys.argv[1]
    percentage = sys.argv[2]

    print(f"Retrain with Algorithm: {algorithm}, Percentage: {percentage}")

    file_path = '/data1/visitor/FSE-Eval/logAE/retrain-rq3.yaml'
    output_path = "/data1/visitor/FSE-Eval/logAE/retrain-rq3-cluster.yaml"

    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    data['head_or_tail'] = algorithm
    data['percentage'] = float(percentage)
    data['exp_dir'] = f"/data1/visitor/FSE-Eval/logAE/after_retrain_exps/arch2_retrain_{algorithm}_{percentage}"

    with open(output_path, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

    print(f"Update Retrain Config to {output_path}")


