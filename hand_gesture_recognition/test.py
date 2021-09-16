# id_list = ["muzi", "frodo", "apeach", "neo"]
# k =2
# report =  ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#
# def solution(id_list, report, k):
#     answer = []
#     dic = {}
#     ans = {}
#     for id in id_list:
#         dic[id] = dic.get(id, 0)
#         ans[id] = ans.get(id, 0)
#
#     # 중복 제거
#     report = list(set(report))
#     # 신고당한 횟수
#     for r in range(len(report)):
#         for i in range(len(id_list)):
#             if report[r].split()[1] == id_list[i]:
#                 dic[id_list[i]] += 1
#     print(dic)
#
#     # 정지된 아이디에 대한 이메일 (신고한 유저에게)
#     for r in range(len(report)):
#         for i in range(len(id_list)):
#             if dic[id_list[i]] >= k and report[r].split()[1] == id_list[i]:
#                 ans[report[r].split()[0]] += 1
#     print(ans)
#
#     answer = ans.values()
#     return answer
#
# print(solution(id_list, report, k))
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
def solution(board, skill):
    answer = 0
    for i in range(len(skill)):
        for n in range(skill[i][1], skill[i][3]):
            for m in range(skill[i][2], skill[i][4]):
                if skill[i][0] == 1:
                    board[n][m] - skill[i][5]
                else:
                    board[n][m] + skill[i][5]

    for N, M in board:
        if board[N][M] > 0:
            answer += 1
    return answer

print(solution(board, skill))