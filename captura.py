
import pyautogui
import sounddevice as sd
import numpy as np
from moviepy.editor import concatenate

# Configuración de la grabación de pantalla
screen_width, screen_height = pyautogui.size()
fps = 30
duration = 10  # Duración de la grabación en segundos

# Configuración de la grabación de audio
sample_rate = 44100
channels = 2
audio_duration = duration

# Capturar pantalla
screen_frames = []
for _ in range(duration * fps):
    img = pyautogui.screenshot()
        frame = np.array(img)
            screen_frames.append(frame)

            # Grabar audio
            audio_frames = sd.rec(int(audio_duration * sample_rate), samplerate=sample_rate, channels=channels)
            sd.wait()

            # Crear archivo de video
            video_clip = concatenate([clip.set_duration(1/fps) for clip in screen_frames])
            video_clip.write_videofile("captura_pantalla.mp4", fps=fps)

            # Crear archivo de audio
            audio_clip = concatenate([clip.set_duration(1/sample_rate) for clip in audio_frames])
            audio_clip.write_audiofile("grabacion_audio.wav")
            ```

            Antes de ejecutar este programa, asegúrate de tener instaladas las bibliotecas necesarias. Puedes instalarlas utilizando el siguiente comando en tu terminal:

            ```
            pip install pyautogui sounddevice moviepy
            ```

            Recuerda que el uso de este programa debe cumplir con las leyes y regulaciones locales, y siempre respeta los derechos de autor y la privacidad de los demás al utilizar cualquier contenido capturado o grabado.Claro, aquí tienes un ejemplo de un programa Python que utiliza las bibliotecas `pyautogui` y `sou
                        import pyautogui
                        import sounddevice as sd
                        import numpy as np
                        from moviepy.editor import concatenate

                        # Configuración de la grabación de pantalla
                        screen_width, screen_height = pyautogui.size()
                        fps = 30
                        duration = 10  # Duración de la grabación en segundos

                        # Configuración de la grabación de audio
                        sample_rate = 44100
                        channels = 2
                        audio_duration = duration

                        # Capturar pantalla
                        screen_frames = []
                        for _ in range(duration * fps):
                            img = pyautogui.screenshot()
                                frame = np.array(img)
                                    screen_frames.append(frame)

                                    # Grabar audio
                                    audio_frames = sd.rec(int(audio_duration * sample_rate), samplerate=sample_rate, channels=channels)
                                    sd.wait()

                                    # Crear archivo de video
                                    video_clip = concatenate([clip.set_duration(1/fps) for clip in screen_frames])
                                    video_clip.write_videofile("captura_pantalla.mp4", fps=fps)

                                    # Crear archivo de audio
                                    audio_clip = concatenate([clip.set_duration(1/sample_rate) for clip in audio_frames])
                                    audio_clip.write_audiofile("grabacion_audio.wav")
                                    ```

                                    Antes de ejecutar este programa, asegúrate de tener instaladas las bibliotecas necesarias. Puedes instalarlas utilizando el siguiente comando en tu terminal:

                                    ```
                                    pip install pyautogui sounddevice moviepy
                                    ```

                                    Recuerda que el uso de este programa debe cumplir con las leyes y regulaciones locales, y siempre respeta los derechos de autor y la privacidad de los demás al utilizar cualquier contenido capturado o grabado.