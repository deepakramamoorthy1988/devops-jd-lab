def get_status():
    return {
        "application": "devops-jd-lab",
        "status": "healthy",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    print(get_status())