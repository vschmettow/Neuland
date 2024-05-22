courses = ['History', 'Maths', 'CompSci', 'P.E.']
courses_2 = ['German', 'Japanese']
nums = [1, 5, 2, 3, 4]

#count number of items
print(len(courses))

#print everything from item 2
print(courses[2:])

#getting last item
print(courses[-2])

#Changing the list

courses.append('Art')

courses.insert(3,'English')
print(courses)

courses.remove('English')
print(courses)

courses.pop()
print(courses)


#adding two lists (extend vs append)
courses.extend(courses_2)
print(courses)

#sorting lists
courses.reverse()
print(courses)

courses.sort()
print(courses)

sorted_courses = sorted(courses)

nums.sort()
print(nums)

#other useful functions - max, min, sum
print(min(nums))

#finding index of value
print(courses.index('Japanese'))

#is this value in the list?
print('Japanese' in courses)

#return index and courses
for index, course in enumerate(courses, start=1):
    print(index, course)

#create a string version of the list
course_str = ' - '.join(courses)
print(course_str)

#revert to list
new_list = course_str.split(' - ')
print(new_list)

#A mutable is when a variable is dependent on another. e.g. courses_2 = courses..
#if you change courses, courses_2 will automatically change too

#Tuple - looks like a list but is immutable.once a tuple is created, its elements cannot be changed. useful for maintaining data integrity
tuple_1 = ('History', 'Math', 'English')
tuple_2 = tuple_1


#Sets - don't care about order, don't allow duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)

print('Math' in cs_courses)
#looks at similarities
print(cs_courses.intersection(art_courses))
#adds two sets
print(cs_courses.union(art_courses))


#Empty things

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()













