import cv2
import base64
from PIL import Image
from dataclasses import dataclass

@dataclass
class ImageStream:
    bytes_img: bytes = None
    data: any = None
    img_name: str = None
    path_img: str = None
    PIL: bool = False

    def open_image(self, img_name: str, img_path: str):
        try:
            self.path_img = img_path
            img = self.path_img + img_name
            self.bytes_img = cv2.imread(img)
            self.img_name = img
            self.PIL = False
            return self.bytes_img
        
        except ValueError:
            return False

    def open_image_PIL(self, img_name, **img_path: str) -> bool:
        try:
            self.path_img = img_path.get("path", "")
            img = self.path_img + img_name
            self.bytes_img = Image.open(rf"{img}")
            self.img_name = img
            self.PIL = True
            return self.bytes_img
        except ValueError:
            return False

    def find_qr(self) -> any:
        if self.PIL:
            return None
        detector = cv2.QRCodeDetector()
        try:
            self.data, found, _ = detector.detectAndDecode(self.bytes_img)
            if found is None:
                return None

            if self.data == "":
                self.data = None
            return self.data

        except ValueError:
            return None

    def display(self) -> None:
        if self.PIL:
            return None
        cv2.imshow("", self.bytes_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def display_PIL(self) -> None:
        if self.PIL is False:
            return None
        self.bytes_img.show()

    def get_data(self) -> any:
        return self.data

    def get_image(self) -> bytes:
        return self.bytes_img

    def get_image_name(self) -> str:
        return self.img_name

    def b64enc(self) -> bytes:
        if self.PIL is False:
            return ""
        with open(self.path_img + self.img_name, "rb") as img:
            return base64.b64encode(img.read())

    def b64dec(self, **data: any) -> bytes:
        if self.PIL is False:
            data = data.get("data", "")
        else:
            data = data.get("data", self.data)

        self.data = base64.b64decode(data)
        return self.data

    def reset(self) -> None:
        self.bytes_img = None
        self.data = None

    def find_qr_in_camera(self, **options: dict) -> any:
        if self.PIL:
            return None
        video = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        self.data = None
        while True:
            _, img = video.read()
            self.data = detector.detectAndDecode(img)[0]

            if self.data:
                video.release()
                cv2.destroyAllWindows()
                return self.data

            if options.get("showCamera", False):
                cv2.imshow("NextQR - ScanningQR", img)
                if cv2.waitKey(1) == ord("-"):
                    break

        video.release()
        cv2.destroyAllWindows()
