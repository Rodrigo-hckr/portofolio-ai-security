import asyncio
import argparse
import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def scan_port(host: str, port: int, semaphore: asyncio.Semaphore) -> None:
    """Intenta conectarse a un puerto específico."""
    async with semaphore:
        try:
            # Aquí iría tu lógica con asyncio.open_connection
            # Ejemplo simulado:
            logging.info(f"Escaneando puerto {port}...")
            pass
        except Exception as e:
            pass

async def main(host: str, start_port: int, end_port: int):
    """Función principal que orquesta el escaneo."""
    semaphore = asyncio.Semaphore(100) # Límite de 100 conexiones concurrentes
    tasks = []
    for port in range(start_port, end_port + 1):
        tasks.append(scan_port(host, port, semaphore))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Async Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or Hostname")
    parser.add_argument("-p", "--ports", default="1-100", help="Port range (e.g., 1-1000)")
    
    args = parser.parse_args()
    
    # Parsear el rango de puertos
    start_port, end_port = map(int, args.ports.split('-'))
    
    logging.info(f"Iniciando escaneo en {args.target}...")
    asyncio.run(main(args.target, start_port, end_port))
    logging.info("Escaneo finalizado.")
