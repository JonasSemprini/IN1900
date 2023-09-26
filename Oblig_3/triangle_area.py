def triangle_area(vertices): #main function
    x1 = vertices[0][0] #x-coordinate of the v1 vector
    y1 = vertices[0][1] #y-coordinate of the v1 vector
    x2 = vertices[1][0] #x-coordinate of the v2 vector
    y2 = vertices[1][1] #y-coordinate of the v2 vector
    x3 = vertices[2][0] #x-coordinate of the v3 vector
    y3 = vertices[2][1] #y-coordinate of the v3 vector
    A = 0.5*(abs((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)+(x2*y1))) #area of the triangle
    return A

def test_triangle_area(): #test function
    v1 = (0,0) #x1 and y1
    v2 = (1,0) #x2 and y2
    v3 = (0,2) #x3 and y3
    vertices = [v1, v2, v3]
    expected = 1 #expected output
    computed = triangle_area(vertices) #calculated output when usin the main function
    tol = 1e-14 #tolerance
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg
test_triangle_area()


"""
Output: python triangle_area.py


Note:
Same as the half_wave exercise. The output in the terminal is blank for any
argument not fulfilling the success statement in the test function. Otherwise
there will be an assertion error. 
"""
