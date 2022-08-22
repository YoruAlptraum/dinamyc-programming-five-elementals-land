# elements:
# gold > wood > earth > water > fire > gold
# the chosen element will cost 1
# the weaker element will cost 0
# the stronger element will cost 2
# obstacles cannot be crossed
g = 2 # gold
t = 1 # wood/tree
e = 0 # earth
w = 1 # water
f = 1 # fire
o = 100 # obstacle
# map dimensions
wid = 20
hei = 20
# the map
map = [
  [0,g,w,o,w,e,t,f,g,f,t,t,t,t,t,t,o,g,o,g],
  [e,e,e,w,t,f,o,f,t,e,t,g,g,e,e,e,e,o,w,w],
  [f,t,o,e,w,t,e,e,g,e,t,t,t,e,e,e,o,f,o,f],
  [f,t,g,t,t,t,o,t,w,g,t,t,t,e,e,e,e,g,w,w],
  [g,w,e,e,e,f,g,w,o,t,t,f,f,o,t,t,t,g,w,w],
  [e,o,w,w,w,f,e,e,o,w,o,f,t,t,o,o,e,g,o,g],
  [t,w,w,t,g,t,e,e,f,o,o,e,f,g,e,e,f,e,g,o],
  [e,f,t,o,f,t,f,g,e,o,t,t,t,f,t,f,o,g,g,t],
  [e,o,w,f,o,o,t,g,e,e,g,g,o,f,w,t,g,g,f,w],
  [w,f,w,e,t,g,w,g,w,e,f,f,w,w,f,e,o,t,t,w],
  [f,o,g,e,t,o,e,t,w,g,g,f,g,f,w,f,t,f,e,g],
  [t,w,w,f,w,e,w,g,f,e,t,e,o,f,f,f,g,g,t,w],
  [g,g,o,g,t,g,g,e,t,w,e,t,t,e,g,w,o,g,g,g],
  [t,w,o,f,w,e,w,w,t,w,e,w,w,w,t,f,e,t,o,w],
  [g,t,t,t,o,f,g,g,w,g,o,e,w,w,e,o,e,g,f,t],
  [e,t,e,o,e,g,g,w,g,w,w,g,e,w,o,f,g,e,g,f],
  [w,e,g,o,f,f,o,f,f,o,f,w,o,o,o,o,t,f,t,w],
  [o,f,f,w,e,g,f,e,e,g,o,t,f,t,g,g,o,e,g,o],
  [o,o,w,o,e,t,w,f,f,o,f,t,w,t,e,g,t,t,w,g],
  [w,t,t,e,g,e,f,e,w,f,e,g,w,o,t,e,t,g,w,w]
]
memo = [[None]*wid for i in range(hei)]

# function to print the arrays for visualization
def print_array(a):
  for i in a:
    row = ""
    for j in i:
      # if there is no value
      #   j will be considered 0
      if j == None:
        j = 0
      # if j is less than 100
      #   add the number to the row with 3 digits
      # else
      #   leave a empty space to represent the obstacle
      row += f"{j:03d} " if j < 100 else "    "
    print(row)

def minimum_cost_path(y,x):
  # print the original map
  print("Inicial map:")
  print_array(map)

  # initiate the starting point as value 0
  memo[0][0] = map[0][0]
  # start
  iterate(y,x)

  # print the memo array
  print("Memo:")
  print_array(memo)

def iterate(y,x):  
  paths = {}
  # if inside the array
  #   add the path to the dict of paths
  #   if the path has not yet been visited it's value will be considered 0 # this value is only used to determine the smallest path
  if y > 0:
    paths["top"] = 0 if memo[y-1][x] == None else memo[y-1][x]
  if x < wid-1:
    paths["right"] = 0 if memo[y][x+1] == None else memo[y][x+1]
  if y < hei-1:
    paths["bottom"] = 0 if memo[y+1][x] == None else memo[y+1][x]
  if x > 0:
    paths["left"] = 0 if memo[y][x-1] == None else memo[y][x-1]

  # while there are paths in the array
  #   check the smallest path and 
  #   remove it from the array
  while len(paths) > 0:
    check_path(y, x, min(paths, key=paths.get))
    del paths[min(paths, key=paths.get)]


def check_path(y,x,path):
  # check the paths acording to the path requested
  # if the cell checked has not yet been visited or it's value is greater than the current path cost
  #   update the value in memo to the sum of the current path + the cell value and iterate
  # else 
  #   just ignore the path
  if path == "top":
    # check the top path
    if memo[y-1][x] == None or memo[y-1][x] > memo[y][x] + map[y-1][x]:
      memo[y-1][x] = memo[y][x] + map[y-1][x]
      iterate(y-1,x)
  if path == "right":
    # check the right path
    if memo[y][x+1] == None or memo[y][x+1] > memo[y][x] + map[y][x+1]:
      memo[y][x+1] = memo[y][x] + map[y][x+1]
      iterate(y,x+1)
  if path == "bottom":
    # check the bottom path
    if memo[y+1][x] == None or memo[y+1][x] > memo[y][x] + map[y+1][x]:
      memo[y+1][x] = memo[y][x] + map[y+1][x]
      iterate(y+1,x)
  if path == "left":
    # check the left path
    if memo[y][x-1] == None or memo[y][x-1] > memo[y][x] + map[y][x-1]:
      memo[y][x-1] = memo[y][x] + map[y][x-1]
      iterate(y,x-1)

if __name__ == "__main__":
    minimum_cost_path(0,0)