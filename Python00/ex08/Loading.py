import sys
import time


def ft_tqdm(lst: range) -> None:
    """
    fonction to display a progress bar
    """
    all = len(lst)
    bar_len = 65
    # to know when we start for the time elapsed
    start_time = time.time()
    # i for the %
    i = 0

    for element in lst:
        elapsed = time.time() - start_time
        # percent on fait le nombre d'element deja traite / par le total
        percent = (i + 1) / all
        # la len * le % des elements deja traite pour remplir la barre
        bar_to_fill = int(bar_len * percent)

        # sinon je faisais /0 et c'est illegal
        if elapsed > 0:
            speed = (i + 1) / elapsed
        else:
            speed = 0

        # if speed > 0:
        #     remaining = (all - (i + 1)) / speed
        # else:
        #     remaining = 0

        percent_txt = f'{int(percent * 100):3d}%'
        bar = '█' * bar_to_fill + ' ' * (bar_len - bar_to_fill)
        count = f'{i + 1}/{all}'

        elapsed_txt = time.strftime("%H:%M:%S", time.gmtime(elapsed))
        # remaining_text = time.strftime("%H:%M:%S", time.gmtime(remaining))
        speed_text = f"{speed:6.2f}it/s"

        # c'est genre le std::cout du python, print ajoute un \n a la fin
        sys.stdout.write(
            f'\r{percent_txt}|{bar}| {count} [{elapsed_txt}, {speed_text}]'
        )
        # ca va un peu plus vite car python gard epas en buffer
        sys.stdout.flush()

        # renvois element temporairement comme un return mais qui stop pas
        yield element
        i += 1
    print()
    return None


# Pour Louise du future, remaining et remaining txt sont commente
# car ca affiche plusieurs lignes sinon, a regler
