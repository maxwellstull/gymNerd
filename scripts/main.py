from nicegui import ui


with ui.row():
    with ui.column():
        with ui.row():
            main = "Chest"
            subA = "Clavical"
            subB = "Sternal"
            subC = "Abdominal"

            m1 = ui.checkbox(main)
            subA1 = ui.checkbox(subA)
            subA1.bind_enabled_from(m1, "value")
            subA1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subB1 = ui.checkbox(subB)
            subB1.bind_enabled_from(m1, "value")
            subB1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subC1 = ui.checkbox(subC)
            subC1.bind_enabled_from(m1, "value")
            subC1.bind_value_from(m1, "value", backward=lambda x: x & False)
        with ui.row():
            main = "Arm"
            subA = "Bicep"
            subB = "Tricep"
            subC = "Forearm"

            m1 = ui.checkbox(main)
            subA1 = ui.checkbox(subA)
            subA1.bind_enabled_from(m1, "value")
            subA1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subB1 = ui.checkbox(subB)
            subB1.bind_enabled_from(m1, "value")
            subB1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subC1 = ui.checkbox(subC)
            subC1.bind_enabled_from(m1, "value")
            subC1.bind_value_from(m1, "value", backward=lambda x: x & False)
    with ui.column():
        with ui.row():
            main = "Shoulder"
            subA = "Anterior"
            subB = "Lateral"
            subC = "Posterior"

            m1 = ui.checkbox(main)
            subA1 = ui.checkbox(subA)
            subA1.bind_enabled_from(m1, "value")
            subA1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subB1 = ui.checkbox(subB)
            subB1.bind_enabled_from(m1, "value")
            subB1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subC1 = ui.checkbox(subC)
            subC1.bind_enabled_from(m1, "value")
            subC1.bind_value_from(m1, "value", backward=lambda x: x & False)
        with ui.row():
            main = "Core"
            subA = "Abdominis"
            subB = "Oblique"
            subC = "Serratus"

            m1 = ui.checkbox(main)
            subA1 = ui.checkbox(subA)
            subA1.bind_enabled_from(m1, "value")
            subA1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subB1 = ui.checkbox(subB)
            subB1.bind_enabled_from(m1, "value")
            subB1.bind_value_from(m1, "value", backward=lambda x: x & False)
            subC1 = ui.checkbox(subC)
            subC1.bind_enabled_from(m1, "value")
            subC1.bind_value_from(m1, "value", backward=lambda x: x & False)



"""
with ui.row():
    groups = ui.scroll_area().classes("w-32 h-64 border")
    muscles = ui.scroll_area().classes("w-32 h-64 border")

    with groups:
        chest = ui.checkbox("Chest")

    with muscles:
        upper = ui.checkbox("upper", value=False)
        upper.bind_visibility_from(chest,"value")
        mid = ui.checkbox("mid", value=False)
        mid.bind_visibility_from(chest,"value")
        lower = ui.checkbox("lower", value=False)
        lower.bind_visibility_from(chest,"value")
"""


ui.run()