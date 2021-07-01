# Kubeflow 

Google Open source platform designed to work on top of kubernetes 
Set of tools addressing ML life cycle stages
- Data exploration
- Feature engineering
- Feature transformation
- Model experimentation
- Model training
- Model evaluation
- Model tuning
- Model serving
- Model versioning

kubeflow takes advantage of the benefits that a kubernetes cluster provides such as container orchestration and auto-scaling.
interacting with kubeflow from the UI

## Kubeflow project

xxx.yaml
environment variables corresponding to the version of kubeflow that we installed:
$ MANIFEST_BRANCH=${MANIFEST_BRANCH:-v1.2-branch}
$ export MANIFEST_BRANCH
$ MANIFEST_VERSION=${MANIFEST_VERSION:-v1.2.0}
$ export MANIFEST_VERSION

Define the project name/configuration directory/yaml files for each service will be allocated:
$ KF_PROJECT_NAME=${KF_PROJECT_NAME:-hello-kf-${PLATFORM}}
$ export KF_PROJECT_NAME
$ mkdir "${KF_PROJECT_NAME}"
$ pushd "${KF_PROJECT_NAME}"

Declare manifest repository. Assign it to an environment variable:
$ manifest_root=https://raw.githubusercontent.com/kubeflow/manifests
$ FILE_NAME=kfctl_k8s_istio.${MANIFEST_VERSION}.yaml
$ KFDEF=${manifest_root}${MANIFEST_BRANCH}/kfdef/${FILE_NAME}

Apply the manifest for deploying our kubeflow project:  ~30 minutes
>kfctl apply -f $KFDEF -V

## more

- https://www.kubeflow.org/
- https://kubernetes.io/
- https://minikube.sigs.k8s.io/docs/start/
- https://minikube.sigs.k8s.io/docs/drivers/hyperkit/
- https://towardsdatascience.com/kubeflow-how-to-install-and-launch-kubeflow-on-your-local-machine-e0d7b4f7508f