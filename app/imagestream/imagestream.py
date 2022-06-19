import cv2
import base64
from PIL import Image
from dataclasses import dataclass


@dataclass
class ImageStream:
    bytes_img: bytes = None
    data: any = None
    img_name: str = None
    PIL: bool = False

    def open_image(self, img_name):
        try:
            self._bytes = cv2.imread(img_name)
            self._imgname = img_name
            self._PIL = False
            return self._bytes

        except ValueError:
            return False

    def open_image_PIL(self, img_name, **img_path: str) -> bool:
        try:
            self.path_img = img_path.get("path", "")
            img = self.path_img + img_name
            self._bytes = Image.open(rf"{img}")
            self._imgname = img
            self._PIL = True
            return self._bytes
        except ValueError:
            return False

    def search_qr(self) -> any:
        if self._PIL:
            return False
        detector = cv2.QRCodeDetector()
        try:
            self._qrdata, found, _ = detector.detectAndDecode(self._bytes)
            if not self._qrdata or found is None:
                self._qrdata = None
                return False

            return self._qrdata

        except ValueError:
            return None

    def display(self):
        if self._PIL:
            return
        cv2.imshow("", self._bytes)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def display_PIL(self) -> None:
        if self._PIL is False:
            return None
        self._bytes.show()

    def get_data(self) -> any:
        return self._qrdata

    def get_image(self) -> bytes:
        return self._bytes

    def get_image_name(self) -> str:
        return self._imgname

    def b64enc(self) -> bytes:
        if self._PIL is False:
            return ""
        with open(self.path_img + self._imgname, "rb") as img:
            return base64.b64encode(img.read())

    def b64dec(self, **data: any) -> bytes:
        if self._PIL is False:
            data = data.get("data", "")
        else:
            data = data.get("data", self._qrdata)

        self._qrdata = base64.b64decode(data)
        return self._qrdata

    def reset(self) -> None:
        self._bytes = None
        self._qrdata = None

    def search_qr_in_camera(self, showcamera: bool = True, windowname: str = ""):
        video = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        self._qrdata = None
        while True:
            img = video.read()[1]
            self._qrdata = detector.detectAndDecode(img)[0]

            if self._qrdata:
                video.release()
                cv2.destroyAllWindows()
                return self._qrdata

            if showcamera:
                cv2.imshow(windowname, img)
                if cv2.waitKey(1) == ord("-"):
                    break

        video.release()
        cv2.destroyAllWindows()
