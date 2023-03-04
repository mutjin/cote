"""
문제
 
$N$개의 전구가 있고 맨 왼쪽에 있는 전구를 첫 번째라고 하자. 전구의 상태는 두 가지가 있으며 이를 숫자로 표현한다.

 
$1$은 전구가 켜져 있는 상태를 의미하고, 
$0$은 전구가 꺼져 있는 상태를 의미한다.

전구를 제어하는 명령어가 1번부터 4번까지 4개가 있다. 아래 표는 각 명령어에 대한 설명이다.

1번 명령어 [
$i$ 
$x$] 
$(1 \le i \le N, 0 \le x \le 1)$ 	 
$i$ 번째 전구의 상태를 
$x$로 변경한다.
2번 명령어 [
$l$ 
$r$] 
$(1 \le l \le r \le N)$ 	 
$l$번째부터 
$r$번째까지의 전구의 상태를 변경한다. (켜져있는 전구는 끄고, 꺼져있는 전구는 킨다.)
3번 명령어 [
$l$ 
$r$] 
$(1 \le l \le r \le N)$ 	 
$l$번째부터 
$r$번째까지의 전구를 끈다.
4번 명령어 [
$l$ 
$r$] 
$(1 \le l \le r \le N)$ 	 
$l$번째부터 
$r$번째까지의 전구를 킨다.
주어지는 명령어를 다 수행한 결과 전구는 어떤 상태인지 알아보자.

입력
첫 번째 줄에 전구의 개수 
$N$와 입력되는 명령어의 개수 
$M$이 주어진다.

두 번째 줄에는 
$N$개의 전구가 현재 어떤 상태 
$s$인지 주어진다. (
$0$은 꺼져있는 상태, 
$1$은 켜져있는 상태)

 
$3$ 번째 줄부터 
$M + 2$ 번째 줄까지 세 개의 정수 
$a, b, c$가 들어온다.

 
$a$는 
$a$번째 명령어를 의미하고 
$b, c$는 
$a$가 1인 경우는 각각 
$i, x$를 의미하고 
$a$가 
$2, 3, 4$ 중 하나면 각각 
$l, r$을 의미한다.

출력
모든 명령어를 수행한 후 전구가 어떤 상태인지 출력한다.

제한
 
$1 \le N, M \le 4,000$ 
 
$1 \le a \le 4$ 
 
$0 \le s, x \le 1$ 
 
$1 \le l \le r \le N$ 
 
$1 \le i \le N$ 
"""

n,m=map(int,input().split()) #전구개수, 명령어개수
bulbs=[0]+list(map(int,input().split())) #전구 상태

for _ in range(m):
    a,b,c=map(int,input().split()) 
    if a==1:
        bulbs[b]=c
    elif a==2:
        for i in range(b,c+1):
            if bulbs[i]==1:
                bulbs[i]=0
            else:
                bulbs[i]=1
    elif a==3:
        for i in range(b,c+1):
            bulbs[i]=0
    else:
        for i in range(b,c+1):
            bulbs[i]=1

for bulb in bulbs[1:]:
    print(bulb,end=" ")