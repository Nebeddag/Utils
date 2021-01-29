def get_balanced_df(dataset_path):
    cl_dirs = os.listdir(dataset_path)
    #Loading images paths
    max_files_cnt = 0
    files_all = []
    frames = []
    for cl_dir in cl_dirs:
        files = os.listdir(os.path.join(dataset_path, cl_dir))
        if len(files) > max_files_cnt:
            max_files_cnt = len(files)
        path = [os.path.join(cl_dir, f) for f in files]
        files_all.append(path)

    #Balance classes
    for i, files in enumerate(files_all):
        n = max_files_cnt // len(files)
        data = {'path': files*n, 'label': np.full(len(files)*n, i).astype(np.int8)}
        df = pd.DataFrame(data)
        frames.append(df)

    #Getting dataframe
    df = pd.concat(frames)
    return df