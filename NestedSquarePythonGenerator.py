import c4d

op: c4d.BaseObject # The python generator

def main() -> c4d.BaseObject:
    # Change this to a constant value if you so desire
    radius = op[c4d.ID_USERDATA,1]

    one_third_radius = radius / 3.0

    points = []
    polys = []

    # Points for inner square (one third of the radius)
    points.append(c4d.Vector(-one_third_radius, one_third_radius, 0))
    points.append(c4d.Vector(one_third_radius, one_third_radius, 0))
    points.append(c4d.Vector(one_third_radius, -one_third_radius, 0))
    points.append(c4d.Vector(-one_third_radius, -one_third_radius, 0))

    # Poly for inner square
    polys.append(c4d.CPolygon(0, 1, 2, 3))

    # Points for outer bounds
    points.append(c4d.Vector(-radius, radius, 0))
    points.append(c4d.Vector(radius, radius, 0))
    points.append(c4d.Vector(radius, -radius, 0))
    points.append(c4d.Vector(-radius, -radius, 0))

    # Polys for outer bounds
    polys.append(c4d.CPolygon(0, 4, 5, 1))
    polys.append(c4d.CPolygon(1, 5, 6, 2))
    polys.append(c4d.CPolygon(2, 6, 7, 3))
    polys.append(c4d.CPolygon(3, 7, 4, 0))

    # Create the poly object
    poly_obj = c4d.BaseObject(c4d.Opolygon)

    # Resize and fill accordingly
    poly_obj.ResizeObject(len(points), len(polys))

    for i, point in enumerate(points):
        poly_obj.SetPoint(i, point)

    for i, poly in enumerate(polys):
        poly_obj.SetPolygon(i, poly)

    return poly_obj
