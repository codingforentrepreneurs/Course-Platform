

def get_cloudinary_image_object(instance, 
                                field_name="image",
                                as_html=False,
                                width=1200
                                ):
    if not hasattr(instance, field_name):
         return ""
    image_object = getattr(instance, field_name)
    if not image_object:
        return ""
    image_options = {
        "width": width
    }
    if as_html:
          return image_object.image(**image_options)
    url = image_object.build_url(**image_options)
    return url