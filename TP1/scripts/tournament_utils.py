def print_results(agents):
    print("Results:")
    print(f"{'Agent':18} {'Name':26} {'Rating (μ ± σ)':>14} {'Iteration time':>17}")  # noqa
    for agent in sorted(
    agents, key=lambda x: x.rating.mu - 3 * x.rating.sigma, reverse=True
):
        print(
        f"{str(agent):18} {str(agent.name()):25} {agent.rating.mu:6.2f} ± {agent.rating.sigma:5.2f} {agent.time*1e3:10.4f} ms"
    )
