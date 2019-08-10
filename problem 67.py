import time

triangle = []

file = open("C:/Users/sethh/Documents/computerScienceProjects/projectEuler/p067_triangle.txt", "r")
for line in file: triangle.append([int(i) for i in line.split(" ")])

#inverts entire triangle
def invertTriangle(triangle):
	invertedTriangle = []
	for i in triangle:
		invertedTriangle = [i] + invertedTriangle
	return invertedTriangle



def maxPathSum(triangle):
	#basecase to see if there's only one element left
	if len(triangle)==1:
		print(triangle)
		return triangle
	newBottomTriangle = []
	#adds the bottom row to the maximum value in the row above
	for i in range(len(triangle[1])):
		newBottomTriangle.append(triangle[1][i] + max(triangle[0][i+1],triangle[0][i]))
	#takes out lowest value		
	for times in range(0,2):
			triangle.pop(0)
	triangle = [newBottomTriangle] + triangle
	maxPathSum(triangle)

	

start = time.time()
print(maxPathSum(invertTriangle(triangle)))
end = time.time()
print(end - start)