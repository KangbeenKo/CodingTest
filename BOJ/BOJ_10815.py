# 숫자 카드
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
# 상근이는 숫자 카드 N개를 가지고 있다. 
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 입력 
    # 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
    # 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 
    # 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 
    # 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
    # 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
    # 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
    # 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

# 출력
    # 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

# 예제 입력                     # 예제 출력
    # 5                             # 1 0 0 1 1 0 0 1
    # 6 3 2 10 -10
    # 8
    # 10 9 -5 2 3 4 5 -10

''''''
n = input() # 해당 코드에서는 n, m 값을 입력 받을 이유가 없음... pass 시킬 수 있는 방법이 있을까?
cards = set([int, input().split()][1])
m = input()
isCards = [int, input().split()][1]
for card in isCards:
    print(1, end = ' ') if card in cards else print(0, end = ' ')

# 성공 (메모리: 119984 KB, 시간: 656 ms)