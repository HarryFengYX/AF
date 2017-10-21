from tasks import things
import sort_tasks
sorted_tasks = sort_tasks.many_tasks(things).task_list

while True:
    for t in range(len(sorted_tasks)):
        print([t, sorted_tasks[t], 'days left: '+str(sorted_tasks[t].daysleft)])    
    cmd = input('>>>')
    del sorted_tasks[int(cmd)]