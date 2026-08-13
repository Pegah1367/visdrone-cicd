# VisDrone CI/CD

The primary goal of this project is to practise CI/CD workflows and deployment/integration on an edge computer, rather than to optimize object detection accuracy.

This project uses a trained YOLO object-detection model with automated testing, Docker containerization, GitHub Actions, and Docker Hub deployment.

## Project Structure

- `weights/best.pt` — trained YOLO model
- `tests/test_model.py` — model loading and inference tests
- `tests/assets/test_image.jpg` — image used for testing
- `docs/test_prediction.jpg` — saved inference result
- `Dockerfile` — Docker image configuration
- `.github/workflows/ci.yml` — automated CI/CD workflow

## CI/CD Pipeline

After a push to the `main` branch, the pipeline automatically:

- installs the required dependencies
- runs Flake8 code-quality checks
- runs Pytest
- loads the YOLO model
- performs inference on the test image
- uploads the prediction result as a GitHub Actions artifact
- builds the Docker image
- runs the tests inside the Docker container
- logs in to Docker Hub
- publishes the verified Docker image to Docker Hub

## Automated Tests

The project includes two model tests:

- `test_model_loads` confirms that `best.pt` loads successfully
- `test_model_inference` confirms that the model performs inference on the test image

Successful Docker test result:

```text
tests/test_model.py::test_model_loads PASSED
tests/test_model.py::test_model_inference PASSED

2 passed
```

## Test Image

The following image is used by the automated inference test:

![Test image](tests/assets/test_image.jpg)

## Sample Inference Result

The following image shows the YOLO prediction generated from the test image:

![YOLO inference result](docs/test_prediction.jpg)

## Run Locally with Docker

Build the Docker image:

```bash
docker build -t visdrone-cicd .
```

Run the automated tests inside the container:

```bash
docker run --rm visdrone-cicd
```

Verify that the model is included inside the Docker image:

```bash
docker run --rm visdrone-cicd ls -lh /app/weights
```

The model is stored inside the image at:

```text
/app/weights/best.pt
```

## Docker Hub Deployment

After the CI tests pass, the Docker image is automatically published as:

```text
pegah1367/visdrone-cicd:latest
```

Pull the published image:

```bash
docker pull pegah1367/visdrone-cicd:latest
```

Run the published image:

```bash
docker run --rm pegah1367/visdrone-cicd:latest
```

Docker Hub repository:

https://hub.docker.com/r/pegah1367/visdrone-cicd

## Current Status

- [x] YOLO model added
- [x] Model loading test completed
- [x] Image inference test completed
- [x] GitHub Actions CI configured
- [x] Inference artifact generated
- [x] Docker image built
- [x] Model tested inside Docker
- [x] Docker image published automatically to Docker Hub
- [ ] Webcam inference on the laptop edge device
