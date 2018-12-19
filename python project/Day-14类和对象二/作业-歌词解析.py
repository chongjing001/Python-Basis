class Lyrics(object):
    """歌词类"""

    def __init__(self, time, text):
        self.time = time
        self.text = text.replace("\n","")

    def __gt__(self, other):
        return self.time > other.time

    def __repr__(self):
        return "%.2f: %s" % (self.time, self.text)


class LyricsAnalyzer(object):
    """歌词解析"""

    def __init__(self, song):
        self.__song = song
        self.__all_lyrics = []

    def __analysis_line(self, line):
        lines = line.split("]")
        # 创建歌词对象
        text = lines[-1]
        for time_str in lines[:-1]:
            fen = float(time_str[1:3])
            miao = float(time_str[4:])
            time = fen * 60 + miao
            lyrics = Lyrics(time, text)
            self.__all_lyrics.append(lyrics)

    def __analysis_file(self):
        """解析文件"""
        try:
            with open(self.__song, encoding="utf-8") as f:
                line = f.readline()
                while line:
                    # 处理
                    self.__analysis_line(line)
                    line = f.readline()
                    # print(line)
        except FileNotFoundError:
            pass
    def get_lyrics(self, time):
        """
        根据时间获取歌词
        :param time:时间
        :return:歌词
        """
        if not self.__all_lyrics:
            # 1.解析歌词文件
            self.__analysis_file()

            # 对歌词排序
            self.__all_lyrics.sort(reverse=True)
            # print(self.__all_lyrics)
            
            if not self.__all_lyrics:
                return "没有歌词！！！"
        # 根据时间查找歌词
        for lyrics in self.__all_lyrics:
            if lyrics.time <= time:
                return lyrics.text


la1 = LyricsAnalyzer("lyricsfile")
print(la1.get_lyrics(6))
print(la1.get_lyrics(60))
print(la1.get_lyrics(86))
print(la1.get_lyrics(160))

la2 = LyricsAnalyzer("not")
print(la2.get_lyrics(3))