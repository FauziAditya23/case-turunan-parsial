import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("Produktivitas Gen Z vs Penggunaan Media Sosial")

# Definisi simbol
x, y = sp.symbols('x y')

# Fungsi Produktivitas (disesuaikan dengan studi kasus)
fungsi_str = "-0.4*x**2 - 0.2*y**2 + 0.5*x*y + 5"

try:
    # Parsing fungsi
    f = sp.sympify(fungsi_str)

    # Hitung turunan parsial
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    st.latex(r"f(x, y) = -0.4x^2 - 0.2y^2 + 0.5xy + 5")
    st.latex(r"\frac{\partial f}{\partial x} = " + sp.latex(fx))
    st.latex(r"\frac{\partial f}{\partial y} = " + sp.latex(fy))

    # Input nilai x0 dan y0
    x0 = st.slider("Durasi penggunaan media sosial per hari (jam)", 0.0, 12.0, 4.0)
    y0 = st.slider("Frekuensi membuka aplikasi per hari", 0.0, 50.0, 20.0)

    # Evaluasi nilai
    f_val = f.subs({x: x0, y: y0})
    fx_val = fx.subs({x: x0, y: y0})
    fy_val = fy.subs({x: x0, y: y0})

    st.write("Nilai produktivitas (f(x, y)):", float(f_val))
    st.write("Gradien (∂f/∂x, ∂f/∂y):", f"({float(fx_val):.2f}, {float(fy_val):.2f})")

    # Grafik
    st.subheader("Grafik Produktivitas & Bidang Singgung")
    x_vals = np.linspace(x0 - 3, x0 + 3, 50)
    y_vals = np.linspace(y0 - 15, y0 + 15, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    f_np = sp.lambdify((x, y), f, 'numpy')
    Z = f_np(X, Y)
    Z_tangent = float(f_val) + float(fx_val)*(X - x0) + float(fy_val)*(Y - y0)

    # Plotting
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax.plot_surface(X, Y, Z_tangent, color='red', alpha=0.4)
    ax.set_xlabel("Durasi (jam)")
    ax.set_ylabel("Frekuensi buka aplikasi")
    ax.set_zlabel("Skor Produktivitas")
    ax.set_title("Produktivitas vs Penggunaan Media Sosial")

    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan saat menjalankan aplikasi: {e}")
