# import sys
# import os
# import matplotlib.pyplot as plt


# project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(project_root)

# from src.inflow_performance import InflowWell
# from src.outflow_performance import VLPModel
# from src.well_analysis import NodalAnalysis


# p_e = 300                   # Пластовое давление, бар
# p_w = 30                   # Забойное даление, бар
# k_pr = 1                    # Коэффициент продуктивности, м3/сут/бар
# wellhead_pressure = 50       # Устьевое давление, бар
# hydraulic_loss_coeff = 0.45    # Коэффициент потерь, бар/(м3/сут)
# q_max = 300                 # Максимальный дебит, м3/сут
# time = 10                   # Время, сут

# ipr_well = InflowWell(k_pr, p_e, p_w)
# vlp_model = VLPModel(wellhead_pressure, hydraulic_loss_coeff)

# nodal_analyzer = NodalAnalysis(ipr_well, vlp_model)
# q, p = nodal_analyzer.calculate_nodal_point()

# results = nodal_analyzer.get_results()
# print("Результаты узлового анализа:")
# print(f"Узловой дебит: {results['nodal_rate']:.2f} м3/сут")
# print(f"Узловое давление: {results['nodal_pressure']:.2f} бар")


# nodal_analyzer.plot_results(q_max)


# main.py
import argparse
from src.inflow_performance import InflowWell
from src.outflow_performance import VLPModel
from src.well_analysis import NodalAnalysis, plot_combined


def main():
    # Парсинг аргументов
    parser = argparse.ArgumentParser()
    parser.add_argument("--well", type=str, required=True)
    parser.add_argument("--pressure", type=float, default=250.0)
    args = parser.parse_args()


    ipr_well = InflowWell(
        k_pr=1,
        p_e=args.pressure,
        p_w=100
    )

    vlp_model = VLPModel(
        wellhead_pressure=50,
        hydraulic_loss_coeff=0.2
    )

    # Расчет узловой точки
    analyzer = NodalAnalysis(ipr_well, vlp_model)
    q, p = analyzer.calculate_nodal_point()

    # Построение и сохранение графика
    plot_combined(ipr_well, vlp_model, q_max=300)

    # Вывод результатов
    print(f"\nРезультаты для скважины {args.well}:")
    print(f"Узловой дебит: {q:.2f} м³/сут")
    print(f"Узловое давление: {p:.2f} бар")

if __name__ == "__main__":
    main()
