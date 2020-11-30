import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk


def lc(l, c, r, u0, i0, T):
    tarray = []
    uarray = []
    iarray = []
    urarray=[]
    ularray=[]
    L = 55E-6  # Индуктивность петли (витка), Гн
    C = 5000E-6  # Ёмкость батареи электролитических конденсаторов, Ф
    R = 0.2  # Омическое сопротивление проволоки, Ом
    U0 = 300  # Начальное напряжение на конденсаторах, В
    I0 = 0  # Начальное значение тока, А
    t = 0  # Начальное время, с
    dt = 1.0e-6  # Шаг времени, с
    Tmax = 5.0E-3  # Конечное время вычисления, с

    L = l  # Индуктивность петли (витка), Гн
    C = c  # Ёмкость батареи электролитических конденсаторов, Ф
    R = r  # Омическое сопротивление проволоки, Ом
    U0 = u0  # Начальное напряжение на конденсаторах, В
    I0 = i0  # Начальное значение тока, А
    t = T  # Начальное время, с
    dt = 1.0e-6  # Шаг времени, с
    Tmax = 5.0E-3  # Конечное время вычисления, с

    # Начальные значения
    u = U0
    i = I0

    while (t < Tmax):
        uR = i * R
        di = (u - uR) / L * dt
        du = i / C * dt
        i += di
        u -= du
        t += dt
        urarray.append(i*r)
        tarray.append(t)
        uarray.append(u)
        ularray.append(-u-u*r)

        # Печать результатов расчёта (время, напряжение, ток)
        #print("{0:f} {1:f} {2:f}".format(t, u, i))
    return tarray, uarray, urarray, ularray


def show_plot(l, c, r, u0, i0, T):
    l = float(l)
    c = float(c)
    r = float(r)
    u0 = float(u0)
    i0 = float(i0)
    T = float(T)
    results = lc(l, c, r, u0, i0, T)
    plt.plot(results[0], results[1], label='Uc(t)')
    plt.plot(results[0], results[2], label='Ur(t)')
    plt.plot(results[0], results[3], label='Ul(t)')
    plt.legend()
    plt.savefig("image.png")
    plt.clf()


def show_img(img):
    load_img = Image.open('image.png')
    render_img = ImageTk.PhotoImage(load_img)
    img.configure(image=render_img)
    img.image = render_img
    img.grid(row=7, column=4)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1000x700")

    lbl_l = Label(root, text='L = ')
    lbl_l.grid(row=0, column=0)

    entry_l = Entry(root)
    entry_l.insert(0, '0.0001')
    entry_l.grid(row=0, column=1)

    lbl_l = Label(root, text='C = ')
    lbl_l.grid(row=1, column=0)

    entry_c = Entry(root)
    entry_c.insert(0, '0.001')
    entry_c.grid(row=1, column=1)

    lbl_l = Label(root, text='R = ')
    lbl_l.grid(row=2, column=0)

    entry_r = Entry(root)
    entry_r.insert(0, '0.00002')
    entry_r.grid(row=2, column=1)

    lbl_l = Label(root, text='U0 = ')
    lbl_l.grid(row=3, column=0)

    entry_u0 = Entry(root)
    entry_u0.insert(0, '300')
    entry_u0.grid(row=3, column=1)

    lbl_l = Label(root, text='I0 = ')
    lbl_l.grid(row=4, column=0)

    entry_i0 = Entry(root)
    entry_i0.insert(0, '0')
    entry_i0.grid(row=4, column=1)

    lbl_l = Label(root, text='t = ')
    lbl_l.grid(row=5, column=0)

    entry_t = Entry(root)
    entry_t.insert(0, '0')
    entry_t.grid(row=5, column=1)

    show_plot(entry_l.get(), entry_c.get(), entry_r.get(), entry_u0.get(), entry_i0.get(), entry_t.get())

    load = Image.open('image.png')
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.grid(row=7, column=4)

    btn_confirm = Button(root, text='Confirm', command=lambda: [show_plot(entry_l.get(), entry_c.get(), entry_r.get(), entry_u0.get(), entry_i0.get(), entry_t.get()), show_img(img)])
    btn_confirm.grid(row=6, column=4)


    root.title("Лаб 2. График цепи")
    root.mainloop()