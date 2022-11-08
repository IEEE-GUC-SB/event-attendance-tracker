import imgbbpy
import asyncio
from Member import Member


async def getImageURL(image_name):
    api_key = '81d53054ed69fe81e4fb509d9d877649'
    client = imgbbpy.AsyncClient(api_key)
    image = await client.upload(file=image_name)
    return image.url


def getGeneratedsData(dataframe):
    generated_ids = []
    generated_qrcode_links = []

    for index, values in dataframe.iterrows():
        # creating a member from each row in Excel file
        member = Member(f"IEEE-{index + 1}",
                        values["Name"],
                        values["Email"],
                        values["Phone Number"],
                        values["Participation As"])
        # adding member id
        generated_ids.append(member.id)

        # generating qrcode png image
        qrcode = member.getMemberQRCode()
        image_name = f"{member.name}.png"
        qrcode.png(image_name, "6")
        # generating an url for the png image we got
        image_url = asyncio.run(getImageURL(image_name))
        # adding the image url
        generated_qrcode_links.append(image_url)

    return [generated_ids, generated_qrcode_links]


def editMembersData(dataframe):
    generated_ids, generated_qrcodes = getGeneratedsData(dataframe)
    dataframe.insert(loc=0, column="ID", value=generated_ids)
    dataframe["QR Code"] = generated_qrcodes
