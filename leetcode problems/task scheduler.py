class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count=Counter(tasks)
        max_fre=max(task_count.values())
        max_fre_tasks=sum(1 for count in task_count.values() if count == max_fre)
        interval_needed=(max_fre-1)*(n+1)+max_fre_tasks
        return max(interval_needed,len(tasks))



        
        
