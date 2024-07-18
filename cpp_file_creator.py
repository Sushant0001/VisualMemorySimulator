import subprocess
import os


def create_trace_file(file_name):
	# subprocess.run(["./run_champsim.sh","bimodal-no-no-no-no-lru-1core","0","10000000",file_name])
	pass
	
	

def create_code_file(text):

	file = open("code_file.cpp",'w')
	file.write(str(text))
	file.close()

	if os.path.exists("obj_trace.xz"):
		os.remove("obj_trace.xz")

	current_directory = os.getcwd()
    #run the code
	subprocess.run(["g++","code_file.cpp","-o","object_code"])
    #obtain its trace
	subprocess.run(["pin-3.30-98830-g1d7b601b3-gcc-linux/pin","-t","tracer/obj-intel64/champsim_tracer.so","-o","obj_trace","--","./object_code"])
    #convert into xz file
	subprocess.run(["xz","-v","obj_trace"])
    #run champsim on that trace
	subprocess.run(["./run_champsim.sh","bimodal-no-no-no-no-lru-1core","0","10000000",current_directory+"/obj_trace.xz"])



def replace_lines(file_path, line_numbers, new_lines):
       # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace specific lines
    for line_number, new_line in zip(line_numbers, new_lines):
        lines[line_number - 1] = new_line + '\n'

    # Write back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)



    subprocess.run(["./build_champsim.sh","bimodal","no","no","no","no","lru","1"])
    # subprocess.run(["./build_champsim.sh","bimodal","next_line","no","no","no","lru","1"])

def replace_lines_srrip(file_path, line_numbers, new_lines):
       # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace specific lines
    for line_number, new_line in zip(line_numbers, new_lines):
        lines[line_number - 1] = new_line + '\n'

    # Write back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)



    subprocess.run(["./build_champsim.sh","bimodal","no","no","no","no","srrip","1"])
    # subprocess.run(["./build_champsim.sh","bimodal","next_line","no","no","no","lru","1"])

def read_current_set_way(file_path, line_numbers):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    a=lines[line_numbers[0]-1].split()
    b=lines[line_numbers[1]-1].split()
    return (str(a[len(a)-1]),str(b[len(b)-1]))
