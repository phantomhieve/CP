for _ in range(input()):
    n,m=map(int,raw_input().split())
    min_salary=list(map(int,raw_input().split()))
    company=list();d=dict()
    for i in range(m):
        max_salary,jobs=map(int,raw_input().split())
        company.append([i,jobs,max_salary])
        d[i]=jobs
    get_jobs=list()
    for i in range(n):
        get_jobs.append(raw_input())
    company.sort(key= lambda sal:sal[2],reverse=True)
    ans_jobs,ans_salary,ans_no_jobs=0,0,0
    for i in range(n):
        for j in range(m):
            if(get_jobs[i][company[j][0]]=='1' and company[j][1]>0 and company[j][2]>=min_salary[i]):
                ans_jobs+=1
                ans_salary+=company[j][2]
                company[j][1]-=1
                break
            
    for i in range(m):
        if(d[company[i][0]]==company[i][1]):
            ans_no_jobs+=1
    print ans_jobs,ans_salary,ans_no_jobs
        
            
