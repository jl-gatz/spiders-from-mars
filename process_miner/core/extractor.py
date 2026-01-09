from process_miner.core.model import Process


def extract_process(url: str) -> Process:
    # stub do MVP
    return Process(
        name="Acesso remoto via VPN",
        actors=["Usuário", "Equipe de TI"],
        steps=[
            "Solicitar acesso",
            "Validar vínculo",
            "Criar credenciais",
            "Usuário acessa VPN"
        ]
    )
