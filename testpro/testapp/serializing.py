from.models import user_details,user_additional_data
from rest_framework import serializers

class additional_details(serializers.ModelSerializer):
    class Meta:
        model=user_additional_data
        fields=("address","phone_number")
class serialized_details(serializers.ModelSerializer):
    extra=additional_details()
    class Meta:
        model=user_details
        fields=("pk","name","password","extra")
    def create(self,validated_data):
        added=validated_data.pop("extra")
        print("adddddd",added)
        user=user_details.objects.create(**validated_data)
        user_additional_data.objects.create(add=user,**added)
        return user
    def update(self, instance, validated_data):
        added= validated_data.pop('extra')
        all_added =instance.extra
        print("all_added",all_added)
        listed= all_added
        print("listed",listed)
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        listed.address=added.get("address",listed.address)
        listed.phone_number=added.get("phone_number",listed.phone_number)
        listed.save()
        return instance 
#//////////////////////////////////////////// forenkey//////////////////////////////////////
    # def create(self, validated_data):
    #     albums_data = validated_data.pop('album_musician')
    #     musician = Musician.objects.create(**validated_data)
    #     for album_data in albums_data:
    #         Album.objects.create(artist=musician, **album_data)
    #     return musician

    # def update(self, instance, validated_data):
    #     albums_data = validated_data.pop('album_musician')
    #     albums = (instance.album_musician).all()
    #     albums = list(albums)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.instrument = validated_data.get('instrument', instance.instrument)
    #     instance.save()

    #     for album_data in albums_data:
    #         album = albums.pop(0)
    #         album.name = album_data.get('name', album.name)
    #         album.release_date = album_data.get('release_date', album.release_date)
    #         album.num_stars = album_data.get('num_stars', album.num_stars)
    #         album.save()
    #     return instance