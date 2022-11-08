# coding: utf-8

from sigma_chan_getter_robo.post_process.io import S3Storage
import pytest
import json

class TestS3Storage:
    """S3 storage test"""
    def test_init(self):
        """S3 test initialization test"""
        s3 = S3Storage("s3", "", "getter-robo", "http://localhost:9000/", "sigma-chan", "sigma-chan-dayo", "")
        assert isinstance(s3, S3Storage)

    def test_fixture(self, mock_s3_minio):
        """S3 test initialization test testing fixture"""
        assert isinstance(mock_s3_minio, S3Storage)


    @pytest.mark.parametrize("texts", ["hoge", "{\"dict\": {\"piyo\": \"fuga\"}}"])
    def test_text_save(self, mock_s3_minio, texts):
        """Test saving some texts.

        Args:
            mock_s3_minio (_type_): _description_
        """
        ### data save to the bucket
        obj_key = "hoge/hoge.json"
        mock_s3_minio.save_data(texts.encode("utf-8"), obj_key)

        ### counting the number of the file to validate
        key_list = [obj.key for obj in mock_s3_minio.bucket.objects.all()]

        assert obj_key in key_list

        ### validate the contents
        saved_obj = mock_s3_minio.s3_resource.Object(mock_s3_minio.bucket_name, obj_key)
        saved_obj.delete()

        key_list = [obj.key for obj in mock_s3_minio.bucket.objects.all()]

        assert obj_key not in key_list


    