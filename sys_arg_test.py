
import sys # Bring in the system tool

# sys.argv is automatically a List of what was typed in the terminal
# Item 0 is the file name ('app.py')
# Item 1 is your data ('Adeal')

player_name = sys.argv[1] 
print(f"Server started for user: {player_name}")

#python File_name.py Adeal