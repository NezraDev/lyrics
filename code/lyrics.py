import time

# Define the lyrics content as a list of tuples
lyrics_content = [
    (0, "Maraming beses nangamba, nadapa, tumaya", 0),
    (0, "Naniwala sa mundong madaya, uh", 0),
    (0, "Ano nga ba? Sino nga ba? Ikaw ba? O ako ba?", 0),
    (0, "Hinay lang, wag mabahala — hala", 1),
    (0, "Yah, wag ka nang maniniwala sa paniniwala", 0),
    (0, "Na dapat makipag-unahan sa karera", 0),
    (0, "Kung wala namang karera, dahan-dahan, tahan lang", 0),
    (0, "Kakayanin umpisa pa lang", 0)
]

def print_lyrics(lyrics_content):
    start_time = time.time()
    for timestamp, line, custom_delay in lyrics_content:
        current_time = time.time() - start_time
        if current_time < timestamp:
            time.sleep(timestamp - current_time)

        for word in line.split():
            for char in word:
                print(char, end='', flush=True)
                time.sleep(0.06)
           
            print(' ', end='', flush=True)
            
        print()
        time.sleep(custom_delay)

print_lyrics(lyrics_content)
