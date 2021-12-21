from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageFont


class EStamp:

    def __init__(self, page_no, to_text, on_text, for_text, pdf_path, position_y=50, color=(56, 59, 145)):
        self.page_no = page_no
        self.to_text = to_text
        self.on_text = on_text
        self.for_text = for_text
        self.pdf_path = pdf_path
        self.position_y = position_y
        self.color = color

    def convert_pdf_to_images(self):
        """
        Extract images from PDF
        :rtype: object
        """
        images = convert_from_path(self.pdf_path)
        for i in range(len(images)):
            images[i].save('page' + str(i) + '.jpg', 'JPEG')

    def prepare_stamp_with_text(self, stamp_x, stamp_y):
        """
        Place stamp on given image
        :param stamp_x: X position of the page
        :param stamp_y: Y position of the page
        :return:
        """
        stamp_photo = Image.open("stamp.png")
        draw = ImageDraw.Draw(stamp_photo)
        font = ImageFont.truetype(r'OperatorMono-Book.otf', 35)
        self.draw_text_image(draw, font)
        background = Image.open(f"page{self.page_no}.jpg")
        background.paste(stamp_photo, (stamp_x, stamp_y), stamp_photo)
        return background

    def draw_text_image(self, draw, font):
        """
        Convert text into image
        :param draw: we use stamp photo to draw out text on it.
        :param font: we can change font family with this variable
        """
        draw.text((110, self.position_y), self.to_text, font=font, fill=self.color)
        draw.text((110, self.position_y + 50), self.on_text, font=font, fill=self.color)
        draw.text((110, self.position_y * 2 + 45), self.for_text, font=font, fill=self.color)


if __name__ == '__main__':
    # TODO: Connect with frappe
    e_stamp = EStamp(page_no=3, to_text="Hiren Vadher", on_text="On Text", for_text="For Text", pdf_path="sample.pdf")
    e_stamp.convert_pdf_to_images()
    image_with_stamp = e_stamp.prepare_stamp_with_text(stamp_x=650, stamp_y=2000)
    image_with_stamp.show()
