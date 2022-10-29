# CloudLab profile for deploying Kubernetes with Flannel CNI

General information for what on CloudLab profiles created via GitHub repo can be found in the example repo [here](https://github.com/emulab/my-profile) or in the CloudLab [manual](https://docs.cloudlab.us/cloudlab-manual.html)

Specifically, the goal of this repo is to create a CloudLab profile that allows for one-click creation of a Kubernetes cluster using Flannel CNI.

## User Information

Create a CloudLab experiment using the k8sflannel profile. It's recommended to use at least 3 nodes for the cluster. It has been testsed on m510, xl170, and rs630 nodes (e.g., various Intel architectures, not ARM, so do not choose an ARM node). 

On each node, a copy of this repo is available at:
```
    /local/repository
```

Docker images are store in additional ephemeral cloudlab storage, mounted on each node at:
```
    /mydata
```

## Image Creation

The [```image_setup.sh```](image_setup.sh) script is how the image was created from the base CloudLab Ubuntu 20.04 image.

## Issues and Contributions

If you find any issues with this profile or have feature requests, please create an issue. We welcome contributions via PRs for features other CloudLab k8s users may find useful.
