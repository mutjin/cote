"""
문제
조기 졸업을 꿈꾸는 종욱이는 요즘 핫한 딥러닝을 공부하던 중, 이미지 처리에 흔히 쓰이는 합성곱 신경망(Convolutional Neural Network, CNN)의 풀링 연산에 영감을 받아 자신만의 풀링을 만들고 이를 222-풀링이라 부르기로 했다.

다음은 8×8 행렬이 주어졌다고 가정했을 때 222-풀링을 1회 적용하는 과정을 설명한 것이다

행렬을 2×2 정사각형으로 나눈다.



각 정사각형에서 2번째로 큰 수만 남긴다. 여기서 2번째로 큰 수란, 정사각형의 네 원소를 크기순으로 a4 ≤ a3 ≤ a2 ≤ a1 라 했을 때, 원소 a2를 뜻한다.



2번 과정에 의해 행렬의 크기가 줄어들게 된다.

종욱이는 N×N 행렬에 222-풀링을 반복해서 적용하여 크기를 1×1로 만들었을 때 어떤 값이 남아있을지 궁금해한다.

랩실 활동에 치여 삶이 사라진 종욱이를 애도하며 종욱이의 궁금증을 대신 해결해주자.

입력
첫째 줄에 N(2 ≤ N ≤ 1024)이 주어진다. N은 항상 2의 거듭제곱 꼴이다. (N=2K, 1 ≤ K ≤ 10)

다음 N개의 줄마다 각 행의 원소 N개가 차례대로 주어진다. 행렬의 모든 성분은 -10,000 이상 10,000 이하의 정수이다. 

출력
마지막에 남은 수를 출력한다.
"""

n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

def search2(x,y,size):
    if size==2:
        ans=[lst[x][y],lst[x][y+1],lst[x+1][y],lst[x+1][y+1]]
    else:
        mid=size//2
        ans=[search2(x,y,mid),search2(x,y+mid,mid),search2(x+mid,y,mid),search2(x+mid,y+mid,mid)]
    ans.sort()
    return ans[-2]

print(search2(0,0,n))