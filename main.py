from icrawler.builtin import GoogleImageCrawler
import datetime


now = datetime.datetime.now()
name_folder = now.strftime("%Y-%m-%d %H:%M")

count_images = int(input('Введите количество фотографий '))
name = str(input('Введите запрос по какому запросу парсить фото '))

google_image_crawler = GoogleImageCrawler(
    storage={'root_dir': f"/Users/anikeenko/PycharmProjects/parserPhoto/images/{name_folder}"})

google_image_crawler.crawl(keyword=name, max_num=count_images)
