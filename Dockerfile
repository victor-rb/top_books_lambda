FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ./
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY app.py ./

CMD ["app.lambda_handler"]
