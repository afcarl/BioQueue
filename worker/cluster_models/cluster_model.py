class ClusterModel:
    def alter_attribute(self, attribute):
        raise NotImplementedError

    def cancel_job(self):
        raise NotImplementedError

    def get_cluster_status(self):
        raise NotImplementedError

    def hold_job(self):
        raise NotImplementedError

    def load_template(self):
        raise NotImplementedError

    def query_job_status(self):
        raise NotImplementedError

    def release_job(self):
        raise NotImplementedError

        raise NotImplementedError
