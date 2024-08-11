
iq=[]
for i in range(4):
    s=input()
    iq.append(s)
    
check=False
for i in range(3):
    pager=0
    titik=0
    for j in range(3):
        if iq[i][j]=="#":
            pager+=1
        else:
            titik+=1
        if iq[i+1][j]=="#":
            pager+=1
        else:
            titik+=1
        if iq[i][j+1]=="#":
            pager+=1
        else:
            titik+=1
        if iq[i+1][j+1]=="#":
            pager+=1
        else:
            titik+=1
        if pager==titik:
            continue
        else:
            check=True
if check:
    print("YES")
else:
    print("NO")
# t=int(input())
# for i in range(t):
#     n=int(input())
#     a=input()
#     check=""
#     ans=0
#     checkbool=False
#     for j in range(n):
#         if check==a[j]:
#             if checkbool==True:
#                 ans+=1
#             checkbool = (checkbool==False)
#         else:
#             checkbool=False
#             ans+=1
#         check=a[j]
#     print(ans)
    
# t=int(input())
# for i in range(t):
#     nm=input()
#     for j in range(len(nm)):
#         if nm[j]==" ":
#             n=nm[:j]
#             m=nm[j:]
#             break
#     n=int(n)
#     m=int(m)
#     time=m%n
#     if n>m:
#         print(n-m)
#     else:
#         if time<=n-time:
#             print(time)
#         else:
#             print(n-time)
# # abc=input()
# # check=True
# # for j in range(len(abc)):
# #     if abc[j]==" ":
# #         k=abc[:j]
# #         ab=abc[j:]
# #         break
# # for j in range(len(ab)):
# #     if ab[j]==" ":
# #         a=ab[:j]
# #         b=ab[j:]
# # k=int(k)
# # a=int(a)
# # if a%k!=0:
# #     check=False
# # b=int(b)
# # if check:
# #     print(int(b/k)-int(a/k)+1)
# # else:
# #     print(int(b/k)-int(a/k))