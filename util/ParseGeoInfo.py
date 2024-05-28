import math


class LambertConverter:
    NX = 149  # X축 격자점 수
    NY = 253  # Y축 격자점 수

    def __init__(self):
        self.map_param = self.LamcParameter()

    class LamcParameter:
        def __init__(self):
            self.Re = 6371.00877  # 사용할 지구반경 [ km ]
            self.grid = 5.0  # 격자간격 [ km ]
            self.slat1 = 30.0  # 표준위도 [degree]
            self.slat2 = 60.0  # 표준위도 [degree]
            self.olon = 126.0  # 기준점의 경도 [degree]
            self.olat = 38.0  # 기준점의 위도 [degree]
            self.xo = 210 / self.grid  # 기준점의 X좌표 [격자거리]
            self.yo = 675 / self.grid  # 기준점의 Y좌표 [격자거리]
            self.first = 0

        def initialize(self):
            PI = math.pi
            DEGRAD = PI / 180.0

            self.re = self.Re / self.grid
            self.slat1_rad = self.slat1 * DEGRAD
            self.slat2_rad = self.slat2 * DEGRAD
            self.olon_rad = self.olon * DEGRAD
            self.olat_rad = self.olat * DEGRAD

            self.sn = math.tan(PI * 0.25 + self.slat2_rad * 0.5) / math.tan(PI * 0.25 + self.slat1_rad * 0.5)
            self.sn = math.log(math.cos(self.slat1_rad) / math.cos(self.slat2_rad)) / math.log(self.sn)
            self.sf = math.tan(PI * 0.25 + self.slat1_rad * 0.5)
            self.sf = math.pow(self.sf, self.sn) * math.cos(self.slat1_rad) / self.sn
            self.ro = math.tan(PI * 0.25 + self.olat_rad * 0.5)
            self.ro = self.re * self.sf / math.pow(self.ro, self.sn)
            self.first = 1

    def map_conv(self, lon, lat):
        if self.map_param.first == 0:
            self.map_param.initialize()

        x, y = self.lamcproj(lon, lat)
        return lon, lat, int(x + 1.5), int(y + 1.5)

    def lamcproj(self, lon, lat):
        PI = math.pi
        DEGRAD = PI / 180.0

        ra = math.tan(PI * 0.25 + lat * DEGRAD * 0.5)
        ra = self.map_param.re * self.map_param.sf / math.pow(ra, self.map_param.sn)
        theta = lon * DEGRAD - self.map_param.olon_rad
        if theta > PI:
            theta -= 2.0 * PI
        if theta < -PI:
            theta += 2.0 * PI
        theta *= self.map_param.sn

        # fill here...!
        x = ra  # fill here...!
        y = self.map_param.ro  # fill here...!
        return x, y

    def convert(self, lon, lat):
        _, _, x, y = self.map_conv(lon, lat)
        return x, y


if __name__ == '__main__':
    converter = LambertConverter()

    longitude = 127.10984626401704
    latitude = 35.79607838004897

    x, y = converter.convert(longitude, latitude)

    print(f"Longitude = {longitude}, Latitude = {latitude} ---> X = {x}, Y = {y}")
