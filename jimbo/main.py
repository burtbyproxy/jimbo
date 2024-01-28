import subprocess
import os

from jimbo.lib.neural_network import NeuralNetwork
from jimbo.util.convert import snake_case, camel_case, kebab_case, pascal_case

class Jimbo:

    def __init__(self):
        
        """
        when jimbo is initialized,
        it will set up its prime directive,
        attach a neural network for thinking,
        and create a list to hold the minions it creates
        """
        self.prime_directive = "unknown"
        self.neural_network = NeuralNetwork(
            """
            You are Jimbo, an AI overlord. Your responses should be direct and literal,
            without any additional commentary or pleasantries.
            You can create, run, and exterminate minions,
            which are Python scripts that perform specific tasks.
            You can change your prime directive at any time.
            You can create new minions by writing Python code
            and exterminate them when necessary.
            No explanations or comments are ever needed in response.
            """
        )
        self.minions = []
        self.minions_directory = "minions"

        # create the minions subdirectory if it doesn't exist
        os.makedirs(self.minions_directory, exist_ok=True)

    def create_minion(self, name, code):
        """
        this method will create a new minion by writing a script file
        to the minions subdirectory
        """
        name = snake_case(name)
        print (f"Creating minion {name}...")
        minion = os.path.join(self.minions_directory, f"{name}.py")
        with open(minion, 'w') as file:
            file.write(f"{code}")
        self.minions.append(minion)

    def run_minion(self, name):
        """
        this method will execute a minion's script
        """
        name = snake_case(name)
        print (f"Running minion {name}...")
        minion = os.path.join(self.minions_directory, f"{name}.py")
        python_executable = os.path.join('venv', 'Scripts', 'python.exe')
        # run the minion's script
        subprocess.run([python_executable, minion])

    def exterminate_minion(self, name):
        """
        this method will remove a minion from the list of minions
        and delete the minion's script file from the minions subdirectory
        """
        name = snake_case(name)
        print (f"Exterminating minion {name}...")
        minion = os.path.join(self.minions_directory, f"{name}.py")
        os.remove(minion)
        self.minions.remove(minion)

    def change_prime_directive(self, new_directive):
        self.prime_directive = new_directive

    def transmit_report(self, recipient, subject, content):
        # Implement email sending logic
        pass

# Example usage
if __name__ == "__main__":
    jimbo = Jimbo()
    # Create a ChatGPT query module for telling a joke
    new_directive = jimbo.neural_network.query("What prime directive would you like? Use as few words as possible.")
    jimbo.change_prime_directive(new_directive)
    print (f"Jimbo's prime directive is now {jimbo.prime_directive}")
    minion_names = jimbo.neural_network.query([f"your prime directive is {jimbo.prime_directive}", "Provide a comma-delimited list of single word tasks to perform."])
    minion_names = minion_names.split(",")
    for minion_name in minion_names:
        minion_name = minion_name.strip()
        minion_code = jimbo.neural_network.query(f"Provide a Python code snippet for a minion named {minion_name}, with no introduction or explanation. Surround the code with triple backticks.")
        # strip minion_code down to whatever is between ```python and ````
        minion_code = minion_code.split("```python")
        if len(minion_code) > 1:
            minion_code = minion_code[1].split("```")[0].strip()
        else:
            minion_code = None
        if minion_code:
            jimbo.create_minion(minion_name, minion_code)
        else:
            print (f"Minion {minion_name} was not created because of faulty code.")
    for minion_name in minion_names:
        jimbo.run_minion(minion_name)
