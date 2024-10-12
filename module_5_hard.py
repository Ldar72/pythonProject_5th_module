import hashlib
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return f"<User '{self.nickname}'>"

    def __str__(self):
        return f"{self.nickname}: {self.age}"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname and self.password == other.password
        else:
            return False

    def verify_login(self, nickname, password):
        return self.nickname == nickname and self.password == hash(password)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"<Video '{self.title}'>"

    def __str__(self):
        return f"{self.title}, duration: {self.duration}, time now: {self.time_now}"

    def verify_watchable(self, age):
        return not self.adult_mode or age >= 18


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.verify_login(nickname, password):
                self.current_user = user
                break
        else:
            print("Ошибка входа")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if any(vid.title == video.title for vid in self.videos):
                continue
            else:
                self.videos.append(video)

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_title):
        found_video = next((video for video in self.videos if video.title == video_title), None)
        if found_video is None:
            print("Видео не найдено")
        elif not found_video.verify_watchable(self.current_user.age):
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print(f"Начало воспроизведения видео {found_video.title}")
            from time import sleep
            for i in range(1, found_video.duration + 1):
                sleep(1)
                print(i)
            print("Конец видео")


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
