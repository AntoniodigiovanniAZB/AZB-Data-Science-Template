from config.config import ProjectConfig

def main():
    config = ProjectConfig()
    print(config.args.raw_dataset_name)
    print(config.img_dir)

if __name__ == '__main__':
    main()
