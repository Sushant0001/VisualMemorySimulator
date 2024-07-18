import matplotlib.pyplot as plt

def read_trace_generate_graph():
    hit_rate_list = []
    time_list = []

    access_frame = 1000
    hit_count = 0
    miss_count = 0
    total_access = 0

    #access_list = []

    file = open("results_trace.txt")
    lines = file.readlines()
    for line in lines:
        l = line.split()
        if len(l)>1 and l[1] == "access":
            total_access += 1
            if l[7] == "hit":
                hit_count += 1
            else:
                miss_count += 1

            if total_access%access_frame == 0:
                #hit_rate is the hit rate per 1000 accesses
                hit_rate = hit_count/access_frame

                hit_rate_list.append(hit_rate)
                time_list.append(total_access)

                #hit count is needed for every 1000 accesses so after every 1000 accesses hit count is made 0
                hit_count = 0 
            
    print("total access : ",total_access)
    #return hit_rate_list,time_list
    y_values,x_values=hit_rate_list,time_list
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.xlabel('Accesses')
    plt.ylabel('Hit Rate')
    plt.title('Hit Rate over the Time')
    plt.grid(True)  # Enable grid
    plt.savefig('hit_rate_graph.pdf', format='pdf')
    plt.show()


# # Sample data
# y_values,x_values = read_trace_generate_graph()

# # Plotting the line graph
# plt.plot(x_values, y_values, marker='o', linestyle='-')

# # Adding labels and title
# plt.xlabel('Accesses')
# plt.ylabel('Hit Rate')
# plt.title('Hit Rate over the Time')

# # Displaying the graph
# plt.grid(True)  # Enable grid

# plt.savefig('hit_rate_graph.pdf', format='pdf')
# plt.show()