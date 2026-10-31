import math
import turtle


def setup_screen():
  """تنظیمات اولیه صفحه نمایش"""
  screen = turtle.Screen()
  screen.setup(width=900, height=900)
  screen.bgcolor("#030503")
  screen.title("Resistance Dog - Cybernetic Neon Matrix")
  screen.tracer(0, 0)
  return screen


def bezier_curve(p0, p1, p2, p3, steps=20):
  """محاسبه نقاط منحنی بزیه درجه ۳ برای ایجاد خطوط نرم و طبیعی"""
  points = []
  for i in range(steps + 1):
    t = i / steps
    u = 1 - t
    x = (
        (u**3) * p0[0]
        + 3 * (u**2) * t * p1[0]
        + 3 * u * (t**2) * p2[0]
        + (t**3) * p3[0]
    )
    y = (
        (u**3) * p0[1]
        + 3 * (u**2) * t * p1[1]
        + 3 * u * (t**2) * p2[1]
        + (t**3) * p3[1]
    )
    points.append((x, y))
  return points


def get_polygon_y_bounds(x, poly):
  """محاسبه دقیق بالاترین و پایین‌ترین مرز مجاز Y برای یک X مشخص داخل چندضلعی"""
  y_intersections = []
  n = len(poly)
  for i in range(n):
    x1, y1 = poly[i]
    x2, y2 = poly[(i + 1) % n]
    if (x1 <= x <= x2) or (x2 <= x <= x1):
      if abs(x2 - x1) < 1e-6:
        y_intersections.extend([y1, y2])
      else:
        t = (x - x1) / (x2 - x1)
        if 0.0 <= t <= 1.0:
          y_intersections.append(y1 + t * (y2 - y1))
  if not y_intersections:
    return None
  return min(y_intersections), max(y_intersections)


def draw_filled_poly(t, points, fill_color):
  """رسم و پر کردن چندضلعی بدون خط دور"""
  if not points:
    return
  t.penup()
  t.goto(points[0])
  t.fillcolor(fill_color)
  t.begin_fill()
  for pt in points[1:]:
    t.goto(pt)
  t.goto(points[0])
  t.end_fill()


def draw_glowing_line(
    t, x1, y1, x2, y2, base_color="#00ff66", max_w=4, core=False
):
  """ترسیم خط مستقیم با هاله نئونی کنترل‌شده"""
  passes = [
      (max_w * 2.6, "#001406"),
      (max_w * 1.5, "#003d14"),
      (max_w, base_color),
  ]
  if core:
    passes.append((max(1, max_w * 0.35), "#99ffbb"))

  for width, color in passes:
    t.pensize(width)
    t.pencolor(color)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
  t.penup()


def draw_glowing_curve(t, points, base_color="#00ff66", max_w=4, core=False):
  """ترسیم منحنی چندنقطه‌ای با افکت نئونی چندلایه"""
  if not points:
    return
  passes = [
      (max_w * 2.5, "#001406"),
      (max_w * 1.5, "#004418"),
      (max_w, base_color),
  ]
  if core:
    passes.append((max(1, max_w * 0.35), "#99ffbb"))

  for width, color in passes:
    t.pensize(width)
    t.pencolor(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    for pt in points[1:]:
      t.goto(pt)
  t.penup()


def draw_vertical_matrix_texture(
    t, poly, step=4, hole_poly=None, style="hood"
):
  """تولید بافت خطوط عمودی دیجیتالی دقیقاً در مرزهای هندسی شکل"""
  xs = [p[0] for p in poly]
  min_x, max_x = int(min(xs)), int(max(xs))

  for x in range(min_x, max_x + 1, step):
    bounds = get_polygon_y_bounds(x, poly)
    if not bounds:
      continue
    y_min, y_max = bounds
    if y_max - y_min < 4:
      continue

    # بررسی برخورد با دهانه داخلی هود (برای جلوگیری از رسم خطوط هود روی صورت)
    segments = [(y_min, y_max)]
    if hole_poly:
      h_bounds = get_polygon_y_bounds(x, hole_poly)
      if h_bounds:
        hy_min, hy_max = h_bounds
        new_segs = []
        for s_min, s_max in segments:
          if hy_max <= s_min or hy_min >= s_max:
            new_segs.append((s_min, s_max))
          else:
            if s_min < hy_min:
              new_segs.append((s_min, hy_min))
            if s_max > hy_max:
              new_segs.append((hy_max, s_max))
        segments = new_segs

    for s_min, s_max in segments:
      # ایجاد تنوع نوری و حس حجم سه‌بعدی با تقسیم خطوط به بخش‌های کوچک‌تر
      curr_y = s_min + 2
      while curr_y < s_max - 2:
        seg_len = 8 + (abs(x * 7 + int(curr_y)) % 18)
        next_y = min(curr_y + seg_len, s_max - 2)

        # محاسبه شدت روشنایی بر اساس موقعیت سه‌بعدی روی هود یا بدن
        norm_x = abs(x) / 145.0
        if style == "hood":
          # لبه‌های هود و بالای پیشانی روشن‌تر، بخش‌های میانی تیره‌تر
          if 0.65 < norm_x < 0.92 or curr_y > 110:
            col = "#00cc44" if (x + int(curr_y)) % 3 == 0 else "#006622"
            w = 2 if (x % 8 == 0) else 1
          else:
            col = "#004d1a" if (x % 8 == 0) else "#00260d"
            w = 1
        elif style == "ear":
          col = "#00b33c" if (x % 6 == 0) else "#004015"
          w = 1
        else:  # body
          col = "#003311" if (x % 8 == 0) else "#001a08"
          w = 1

        t.pensize(w)
        t.pencolor(col)
        t.penup()
        t.goto(x, curr_y)
        t.pendown()
        t.goto(x, next_y)

        # فاصله‌های کوچک بین خطوط برای ایجاد حس اسکن‌لاین واقعی
        gap = 3 if (x + int(curr_y)) % 4 == 0 else 1
        curr_y = next_y + gap
  t.penup()


def get_hood_geometry():
  """تولید مختصات دقیق منحنی‌های بیرونی و دهانه داخلی هود"""
  outer = []
  # از پایین چپ هود به سمت بالا و چرخش به راست با منحنی بزیه
  outer.extend(bezier_curve((-55, -130), (-115, -110), (-150, -40), (-142, 45)))
  outer.extend(bezier_curve((-142, 45), (-135, 130), (-75, 175), (0, 175))[1:])
  outer.extend(bezier_curve((0, 175), (75, 175), (135, 130), (142, 45))[1:])
  outer.extend(bezier_curve((142, 45), (150, -40), (115, -110), (55, -130))[1:])
  outer.extend(bezier_curve((55, -130), (20, -142), (-20, -142), (-55, -130))[1:])

  # دهانه تاریک داخل هود (محل قرارگیری صورت سگ)
  inner = []
  inner.extend(bezier_curve((-45, -108), (-92, -85), (-102, -5), (-85, 58)))
  inner.extend(bezier_curve((-85, 58), (-55, 112), (55, 112), (85, 58))[1:])
  inner.extend(bezier_curve((85, 58), (102, -5), (92, -85), (45, -108))[1:])
  inner.extend(bezier_curve((45, -108), (15, -120), (-15, -120), (-45, -108))[1:])

  return outer, inner


def draw_body(t):
  """ترسیم بدن کوچک، تاریک و محوشونده در پس‌زمینه با اتصال طبیعی به زیر هود"""
  body_poly = []
  body_poly.extend(
      bezier_curve((-58, -115), (-85, -155), (-92, -210), (-82, -265))
  )
  body_poly.extend([(-82, -265), (82, -265)])
  body_poly.extend(
      bezier_curve((82, -265), (92, -210), (85, -155), (58, -115))[1:]
  )

  draw_filled_poly(t, body_poly, "#020402")
  draw_vertical_matrix_texture(t, body_poly, step=5, style="body")

  # خطوط بسیار کم‌رنگ دور شانه‌ها تا بدن به صورت یک شکل هندسی جدا دیده نشود
  left_shoulder = bezier_curve(
      (-58, -115), (-85, -155), (-92, -210), (-82, -265)
  )
  right_shoulder = bezier_curve((58, -115), (85, -155), (92, -210), (82, -265))
  draw_glowing_curve(t, left_shoulder, "#004d1a", max_w=2, core=False)
  draw_glowing_curve(t, right_shoulder, "#004d1a", max_w=2, core=False)


def draw_arms(t):
  """ترسیم بازوها و چین‌های آستین در امتداد شانه‌ها"""
  # بازوی چپ
  left_arm = []
  left_arm.extend(
      bezier_curve((-68, -140), (-105, -185), (-115, -235), (-100, -275))
  )
  left_arm.extend([(-100, -275), (-65, -275)])
  left_arm.extend(
      bezier_curve((-65, -275), (-68, -230), (-62, -185), (-48, -145))[1:]
  )

  draw_filled_poly(t, left_arm, "#030603")
  draw_vertical_matrix_texture(t, left_arm, step=5, style="body")
  draw_glowing_curve(t, left_arm[:21], "#00802b", max_w=2, core=False)
  draw_glowing_curve(t, left_arm[22:], "#004d1a", max_w=1, core=False)

  # بازوی راست
  right_arm = []
  right_arm.extend(
      bezier_curve((68, -140), (105, -185), (115, -235), (100, -275))
  )
  right_arm.extend([(100, -275), (65, -275)])
  right_arm.extend(
      bezier_curve((65, -275), (68, -230), (62, -185), (48, -145))[1:]
  )

  draw_filled_poly(t, right_arm, "#030603")
  draw_vertical_matrix_texture(t, right_arm, step=5, style="body")
  draw_glowing_curve(t, right_arm[:21], "#00802b", max_w=2, core=False)
  draw_glowing_curve(t, right_arm[22:], "#004d1a", max_w=1, core=False)


def draw_ears(t):
  """ترسیم گوش‌های نرم و یکپارچه با بالای هود به همراه بافت داخلی محدودشده"""
  # گوش چپ (منحنی نرم متصل به قوس هود)
  left_ear = []
  left_ear.extend(bezier_curve((-122, 75), (-158, 125), (-165, 180), (-132, 202)))
  left_ear.extend(
      bezier_curve((-132, 202), (-102, 212), (-78, 175), (-68, 142))[1:]
  )

  draw_filled_poly(t, left_ear, "#030703")
  draw_vertical_matrix_texture(t, left_ear, step=4, style="ear")
  draw_glowing_curve(t, left_ear, "#00e65c", max_w=3, core=False)

  # گوش راست
  right_ear = []
  right_ear.extend(bezier_curve((122, 75), (158, 125), (165, 180), (132, 202)))
  right_ear.extend(bezier_curve((132, 202), (102, 212), (78, 175), (68, 142))[1:])

  draw_filled_poly(t, right_ear, "#030703")
  draw_vertical_matrix_texture(t, right_ear, step=4, style="ear")
  draw_glowing_curve(t, right_ear, "#00e65c", max_w=3, core=False)


def draw_head(t):
  """ترسیم هود بزرگ و پوشاننده با بافت اسکن‌لاین دقیق و چین‌های پارچه"""
  outer_hood, inner_opening = get_hood_geometry()

  # پر کردن کل حجم هود با رنگ تیره
  draw_filled_poly(t, outer_hood, "#030803")

  # ایجاد بافت متراکم خطوط عمودی که دقیقاً در مرزهای هود و بیرون از حفره صورت قرار دارند
  draw_vertical_matrix_texture(
      t, outer_hood, step=4, hole_poly=inner_opening, style="hood"
  )

  # پر کردن دهانه داخلی هود با مشکی خالص برای ایجاد عمق و کنتراست با صورت
  draw_filled_poly(t, inner_opening, "#010201")

  # خطوط چین و چروک نئونی روی هود برای القای حس حجم پارچه
  left_fold = bezier_curve((-65, 155), (-112, 105), (-122, 10), (-92, -85))
  right_fold = bezier_curve((65, 155), (112, 105), (122, 10), (92, -85))
  draw_glowing_curve(t, left_fold, "#009933", max_w=2, core=False)
  draw_glowing_curve(t, right_fold, "#009933", max_w=2, core=False)

  # درز مرکزی بالای هود
  center_seam = bezier_curve((0, 175), (-3, 145), (-2, 120), (0, 98))
  draw_glowing_curve(t, center_seam, "#00cc44", max_w=2, core=False)

  # کانتور بیرونی هود و لبه داخلی کلاه با درخشش نئونی
  draw_glowing_curve(t, outer_hood, "#00ff66", max_w=4, core=True)
  draw_glowing_curve(t, inner_opening, "#00cc44", max_w=3, core=False)


def draw_eyes(t):
  """ترسیم چشم، پوزه، بینی و جزئیات چهره سگ Resistance Dog در دل تاریکی هود"""
  # ۱. بافت نوری ملایم سمت چپ صورت و گونه که از تاریکی بیرون آمده
  cheek_patch = []
  cheek_patch.extend(bezier_curve((-75, 35), (-82, -15), (-68, -65), (-35, -88)))
  cheek_patch.extend(bezier_curve((-35, -88), (-5, -95), (25, -85), (38, -55))[1:])
  cheek_patch.extend(bezier_curve((38, -55), (25, -10), (-15, 25), (-75, 35))[1:])
  draw_vertical_matrix_texture(t, cheek_patch, step=4, style="ear")

  # ۲. برجستگی پوزه سگ (پوزه متمایل به راست/مرکز مطابق با زاویه کاراکتر)
  snout_bridge = bezier_curve((-22, 12), (-5, -12), (18, -28), (32, -38))
  draw_glowing_curve(t, snout_bridge, "#00ff66", max_w=3, core=True)

  muzzle_lower = bezier_curve((-48, -42), (-25, -82), (18, -85), (36, -50))
  draw_glowing_curve(t, muzzle_lower, "#00cc44", max_w=2, core=False)

  # ۳. بینی سگ (فرم مثلثی نرم و تیره در انتهای پوزه با هایلایت نئونی در لبه بالا)
  nose_poly = []
  nose_poly.extend(bezier_curve((2, -36), (18, -32), (36, -36), (38, -46)))
  nose_poly.extend(bezier_curve((38, -46), (32, -62), (15, -64), (4, -50))[1:])
  nose_poly.extend([nose_poly[-1], nose_poly[0]])

  draw_filled_poly(t, nose_poly, "#001a09")
  draw_glowing_curve(t, nose_poly[:15], "#39ff14", max_w=3, core=True)
  draw_glowing_curve(t, nose_poly[15:], "#00802b", max_w=2, core=False)

  # خط زیر بینی و دهان سگ
  mouth_line = bezier_curve((18, -62), (12, -74), (-8, -78), (-28, -70))
  draw_glowing_curve(t, mouth_line, "#00e65c", max_w=2, core=False)

  # ۴. چشم اصلی شاخص در سمت چپ (بادامی‌شکل و تیز، بدون قاب مستطیلی مصنوعی)
  eye_upper = bezier_curve((-66, 8), (-48, 24), (-24, 18), (-14, 2))
  eye_lower = bezier_curve((-14, 2), (-26, -10), (-50, -8), (-66, 8))
  left_eye = eye_upper + eye_lower[1:]

  draw_filled_poly(t, left_eye, "#00260d")
  draw_glowing_curve(t, left_eye, "#39ff14", max_w=3, core=True)

  # درخشش مردمک و خط نوری داخل چشم
  eye_glow = bezier_curve((-52, 8), (-40, 12), (-28, 9), (-22, 3))
  draw_glowing_curve(t, eye_glow, "#76ff03", max_w=2, core=True)

  # خط ابرو و سایه بالای چشم برای ایجاد حس اخم و تمرکز کاراکتر
  brow_line = bezier_curve((-72, 18), (-50, 34), (-22, 28), (-8, 12))
  draw_glowing_curve(t, brow_line, "#00b33c", max_w=2, core=False)

  # ۵. چشم دوم در سمت راست (نیمه‌پنهان در سایه هود برای حفظ زاویه طبیعی سر)
  right_eye_hint = bezier_curve((18, 8), (32, 15), (48, 12), (56, 2))
  draw_glowing_curve(t, right_eye_hint, "#00802b", max_w=2, core=False)


def draw_neon_details(t):
  """اضافه کردن خطوط اسکن‌لاین برجسته و درخشش‌های نقطه‌ای در لبه‌های هود و یقه"""
  # هایلایت‌های عمودی درخشان روی لبه‌های نورگیر هود
  accents = [
      (-128, -15, 55),
      (-120, -45, 85),
      (-108, -70, 105),
      (128, -15, 55),
      (120, -45, 85),
      (108, -70, 105),
      (-40, 118, 162),
      (0, 115, 170),
      (40, 118, 162),
  ]
  for x, y1, y2 in accents:
    draw_glowing_line(t, x, y1, x, y2, "#39ff14", max_w=2, core=False)

  # خطوط جناغی یقه هودی در زیر چانه
  collar_left = bezier_curve((-45, -112), (-25, -145), (-8, -168), (0, -182))
  collar_right = bezier_curve((45, -112), (25, -145), (8, -168), (0, -182))
  draw_glowing_curve(t, collar_left, "#00b33c", max_w=2, core=False)
  draw_glowing_curve(t, collar_right, "#00b33c", max_w=2, core=False)


def main():
  """تابع اصلی اجرای برنامه با رعایت دقیق ترتیب لایه‌بندی از عقب به جلو"""
  screen = setup_screen()
  t = turtle.Turtle()
  t.hideturtle()
  t.speed(0)

  # ۱. رسم اندام‌های پشتی و بالاتنه تیره
  draw_body(t)
  draw_arms(t)

  # ۲. رسم گوش‌ها (پشت لبه بیرونی کلاه هود قرار می‌گیرند تا اتصال یکپارچه داشته باشند)
  draw_ears(t)

  # ۳. رسم هود اصلی و حفره تاریک میانی
  draw_head(t)

  # ۴. رسم اجزای صورت در داخل دهانه هود و افزودن جزئیات نوری نهایی
  draw_eyes(t)
  draw_neon_details(t)

  screen.update()
  turtle.done()


if __name__ == "__main__":
  main()
