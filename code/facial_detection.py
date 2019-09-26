# 3d cloud points preprocessing

# face curvature maps

def centroid(face_points):
	# do calculations

def matrix_add(m1, m2):
	rows = len(m1)
	cols = len(m1[0])

	for r in range(rows):
		for c in range(cols):
			m1[r][c] += m2[r][c]

def matrix_multiply(x, y, z):
	dims = 3
	m_cov = [[0] * dims for _ in range(dims)]

	m_cov[0][0] = x ** 2
	m_cov[0][1] = x * y
	m_cov[0][2] = x * z

	m_cov[1][0] = x * y
	m_cov[1][1] = y ** 2
	m_cov[1][2] = y * z

	m_cov[2][0] = x * z
	m_cov[2][1] = y * z
	m_cov[2][2] = z ** 2

	return m_cov

def matrix_divide(mat, n):
	rows = len(mat)
	cols = len(mat[0])

	for r in range(rows):
		for c in range(cols):
			mat[r][c] /= n

def covariance(face_points, centroid):
	w_n = len(face_points)
	dims = 3
	m_cov = [[0] * dims for _ in range(dims)]
	(cx, cy, cz) = centroid

	for (x, y, z) in face_points:
		dx = x - cx
		dy = y - cy
		dz = z - cz

		arr = matrix_multiply(dx, dy, dz)
		matrix_add(m_cov, arr)

	matrix_divide(m_cov, w_n)
	return m_cov

# features extraction

# similarity matching