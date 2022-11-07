# coding: utf-8

from sigma_chan_getter_robo.post_process.io import S3Storage

class TestS3Storage:
    def test_init(self):
        s3 = S3Storage("s3", "", "getter_robo", "http://localhost:9000/", "sigma-chan", "sigma-chan-dayo", "")
        assert isinstance(s3, S3Storage)

    def test_fixture(self, mock_s3_minio):
        assert isinstance(mock_s3_minio, S3Storage)

    def test_bucket(self, mock_s3_minio, mock_file_path):
        s3 = mock_s3_minio

        obj_key = "hoge.dat"

        s3.bucket.upload_file(mock_file_path, obj_key)
        
        key_list = [obj.key for obj in s3.bucket.objects.all()]

        assert obj_key in key_list
        
    #def test_text_save(self, mock_s3_minio):
    #    data = "hoge"
    #    mock_s3_minio.save_data(data.encode("utf-8"), "hoge/hoge.dat")