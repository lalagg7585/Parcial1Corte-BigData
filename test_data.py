import unittest
from unittest.mock import Mock, patch
from funcion2_lambda import lambda_handler  # Import your function here


class TestLambdaHandlerProcessing(unittest.TestCase):
    @patch('funcion2_lambda.boto3.client')
    @patch('funcion2_lambda.boto3.resource')
    def test_lambda_handler_processing(
            self, mock_boto3_resource, mock_boto3_client):
        # Simulate the behavior of boto3
        mock_s3_resource = mock_boto3_resource.return_value
        # mock_s3_client = mock_boto3_client.return_value

        # Mock the S3 object and its get method
        mock_s3_object = Mock()
        mock_s3_resource.Object.return_value = mock_s3_object
        mock_s3_object.get.return_value = {
            'Body': Mock(read=Mock(return_value=b"HTML Content"))}

        # Execute the function under test
        result = lambda_handler(None, None)

        # Verify calls and behavior
        self.assertEqual(result['statusCode'], 200)
        # Add more assertions as necessary


if __name__ == '__main__':
    unittest.main()
